#!/usr/bin/env python3
"""
GeckoTerminal OHLCV candlestick data integration for real chart data
Fetches authentic OHLCV candlestick data from GeckoTerminal API
"""

import json
import sys
import time
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

def fetch_ohlcv_data(network_id, pool_address, timeframe='5m', limit=100):
    """
    Fetch real OHLCV candlestick data from GeckoTerminal API
    
    Args:
        network_id: Network identifier (e.g., 'hyperevm', 'ethereum', 'base')
        pool_address: Pool/pair address
        timeframe: '1m', '5m', '15m', '1h', '4h', '1d'
        limit: Number of candles to fetch (max 1000)
    
    Returns:
        List of OHLCV candles with authentic trading data
    """
    try:
        # GeckoTerminal OHLCV endpoint
        url = f"https://api.geckoterminal.com/api/v2/networks/{network_id}/pools/{pool_address}/ohlcv/{timeframe}"
        
        params = f"?limit={limit}&aggregate=1d" if timeframe == '1d' else f"?limit={limit}"
        full_url = url + params
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        }
        
        request = Request(full_url, headers=headers)
        
        with urlopen(request, timeout=15) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                
                if 'data' in data and 'attributes' in data['data']:
                    ohlcv_list = data['data']['attributes'].get('ohlcv_list', [])
                    
                    if ohlcv_list:
                        print(f"✅ Fetched {len(ohlcv_list)} real {timeframe} candles from GeckoTerminal", file=sys.stderr)
                        return parse_ohlcv_candles(ohlcv_list, timeframe)
                    else:
                        print(f"❌ No OHLCV data available for {pool_address}", file=sys.stderr)
                        
            else:
                print(f"❌ GeckoTerminal API error: HTTP {response.status}", file=sys.stderr)
                
    except (URLError, HTTPError, json.JSONDecodeError) as e:
        print(f"GeckoTerminal OHLCV API error: {e}", file=sys.stderr)
        
    return []

def parse_ohlcv_candles(ohlcv_list, timeframe):
    """
    Parse GeckoTerminal OHLCV data into our candlestick format
    
    OHLCV format: [timestamp_unix_ms, open, high, low, close, volume]
    """
    candles = []
    
    for ohlcv in ohlcv_list:
        try:
            if len(ohlcv) >= 6:
                timestamp = int(ohlcv[0])  # Unix milliseconds
                open_price = float(ohlcv[1])
                high_price = float(ohlcv[2])
                low_price = float(ohlcv[3])
                close_price = float(ohlcv[4])
                volume = float(ohlcv[5])
                
                # Skip invalid candles
                if open_price > 0 and high_price > 0 and low_price > 0 and close_price > 0:
                    candle = {
                        "timestamp": timestamp,
                        "open": open_price,
                        "high": high_price,
                        "low": low_price,
                        "close": close_price,
                        "volume": volume,
                        "direction": "up" if close_price >= open_price else "down",
                        "timeframe": timeframe,
                        "source": "GeckoTerminal_Real"
                    }
                    candles.append(candle)
                    
        except (ValueError, IndexError) as e:
            print(f"Error parsing OHLCV candle: {e}", file=sys.stderr)
            continue
    
    # Sort by timestamp (newest first for chart display)
    candles.sort(key=lambda x: x['timestamp'], reverse=True)
    
    print(f"📊 Processed {len(candles)} valid {timeframe} candles", file=sys.stderr)
    return candles

def find_hyperevm_pool_address(token_symbol):
    """
    Try to find the pool address for a token on HyperEVM
    This is a simplified approach - in production you'd maintain a mapping
    """
    # Known pool addresses for major HyperEVM tokens
    known_pools = {
        'BUDDY': '0x123...abc',  # Would need real pool address
        'RUB': '0x456...def',    # Would need real pool address  
        'LHYPE': '0x789...ghi',  # Would need real pool address
        # Add more as discovered
    }
    
    return known_pools.get(token_symbol.upper())

def get_real_chart_data(token_symbol, timeframe='5m', candle_count=60):
    """
    Get real OHLCV chart data for a HyperEVM token
    """
    try:
        # First try to find the pool address
        pool_address = find_hyperevm_pool_address(token_symbol)
        
        if pool_address:
            # Fetch real OHLCV data
            candles = fetch_ohlcv_data('hyperevm', pool_address, timeframe, candle_count)
            
            if candles:
                return {
                    "symbol": token_symbol,
                    "timeframe": timeframe,
                    "candles": candles[:candle_count],  # Limit to requested count
                    "data_source": "GeckoTerminal_Real",
                    "last_updated": time.time()
                }
                
        # Fallback message
        print(f"⚠️  Pool address not found for {token_symbol} on HyperEVM", file=sys.stderr)
        return None
        
    except Exception as e:
        print(f"Error fetching chart data for {token_symbol}: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) > 1:
        symbol = sys.argv[1]
        timeframe = sys.argv[2] if len(sys.argv) > 2 else '5m'
        
        chart_data = get_real_chart_data(symbol, timeframe)
        
        if chart_data:
            print(json.dumps(chart_data, indent=2))
        else:
            print(json.dumps({"error": f"No chart data available for {symbol}"}))
    else:
        print("Usage: python gecko_ohlcv.py <TOKEN_SYMBOL> [TIMEFRAME]")
        print("Example: python gecko_ohlcv.py BUDDY 5m")