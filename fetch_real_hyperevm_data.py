#!/usr/bin/env python3
import requests
import json
import time
from urllib.parse import urljoin

def fetch_dexscreener_hyperevm_data():
    """
    Fetch all real HyperEVM token data from DexScreener API
    """
    try:
        # DexScreener API for HyperEVM tokens
        url = "https://api.dexscreener.com/latest/dex/tokens/hyperevm"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        print("🔍 Fetching real HyperEVM token data from DexScreener...")
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if 'pairs' in data and data['pairs']:
            print(f"✅ Found {len(data['pairs'])} trading pairs on HyperEVM")
            
            tokens = {}
            for pair in data['pairs']:
                if pair.get('chainId') == 'hyperevm':
                    base_token = pair.get('baseToken', {})
                    quote_token = pair.get('quoteToken', {})
                    
                    # Get base token data
                    if base_token.get('symbol') and base_token.get('symbol') != 'HYPE':
                        symbol = base_token.get('symbol')
                        tokens[symbol] = {
                            'symbol': symbol,
                            'name': base_token.get('name', f"{symbol} Token"),
                            'address': base_token.get('address'),
                            'price_usd': float(pair.get('priceUsd', '0')),
                            'price_native': float(pair.get('priceNative', '0')),
                            'volume_24h': float(pair.get('volume', {}).get('h24', 0)),
                            'price_change_24h': float(pair.get('priceChange', {}).get('h24', 0)),
                            'liquidity_usd': float(pair.get('liquidity', {}).get('usd', 0)),
                            'dex_id': pair.get('dexId'),
                            'pair_address': pair.get('pairAddress'),
                            'chain_id': pair.get('chainId')
                        }
            
            print(f"📊 Processed {len(tokens)} unique tokens")
            return tokens
            
        else:
            print("❌ No trading pairs found")
            return {}
            
    except Exception as e:
        print(f"❌ Error fetching DexScreener data: {e}")
        return {}

def fetch_gecko_terminal_hyperevm():
    """
    Fetch HyperEVM token data from Gecko Terminal as backup
    """
    try:
        url = "https://api.geckoterminal.com/api/v2/networks/hyperevm/pools"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        print("🦎 Fetching from Gecko Terminal...")
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        tokens = {}
        if 'data' in data:
            for pool in data['data']:
                attributes = pool.get('attributes', {})
                base_token = attributes.get('base_token_price_usd')
                
                if base_token and attributes.get('base_token_price_usd'):
                    symbol = attributes.get('name', '').split('/')[0].strip()
                    if symbol and symbol != 'HYPE':
                        tokens[symbol] = {
                            'symbol': symbol,
                            'name': f"{symbol} Token",
                            'price_usd': float(attributes.get('base_token_price_usd', '0')),
                            'volume_24h': float(attributes.get('volume_usd', {}).get('h24', 0)),
                            'price_change_24h': float(attributes.get('price_change_percentage', {}).get('h24', 0)),
                            'liquidity_usd': float(attributes.get('reserve_in_usd', 0)),
                            'chain_id': 'hyperevm'
                        }
        
        print(f"🦎 Gecko Terminal found {len(tokens)} tokens")
        return tokens
        
    except Exception as e:
        print(f"❌ Gecko Terminal error: {e}")
        return {}

def main():
    print("🚀 Fetching real HyperEVM token data...")
    
    # Try DexScreener first
    dex_tokens = fetch_dexscreener_hyperevm_data()
    
    # Try Gecko Terminal as backup
    gecko_tokens = fetch_gecko_terminal_hyperevm()
    
    # Combine data (DexScreener takes priority)
    all_tokens = {**gecko_tokens, **dex_tokens}
    
    if all_tokens:
        print(f"\n✅ Successfully fetched {len(all_tokens)} real HyperEVM tokens:")
        
        # Sort by volume for better display
        sorted_tokens = sorted(all_tokens.items(), key=lambda x: x[1].get('volume_24h', 0), reverse=True)
        
        for symbol, data in sorted_tokens:
            price_usd = data.get('price_usd', 0)
            volume_24h = data.get('volume_24h', 0)
            change_24h = data.get('price_change_24h', 0)
            
            change_str = f"+{change_24h:.2f}%" if change_24h > 0 else f"{change_24h:.2f}%"
            volume_str = f"${volume_24h:,.0f}" if volume_24h > 1000 else f"${volume_24h:.2f}"
            
            print(f"  {symbol:8} | ${price_usd:.8f} | {change_str:>8} | Vol: {volume_str}")
        
        # Save to JSON file for the trading platform
        output_data = {
            'timestamp': int(time.time()),
            'tokens': all_tokens,
            'count': len(all_tokens)
        }
        
        with open('real_hyperevm_tokens.json', 'w') as f:
            json.dump(output_data, f, indent=2)
        
        print(f"\n💾 Saved {len(all_tokens)} tokens to real_hyperevm_tokens.json")
        return all_tokens
    
    else:
        print("❌ Failed to fetch any token data")
        return {}

if __name__ == "__main__":
    main()