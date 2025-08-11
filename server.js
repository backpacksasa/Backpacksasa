const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const path = require('path');
const { execSync } = require('child_process');

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
    cors: {
        origin: "*",
        methods: ["GET", "POST"]
    }
});

const PORT = process.env.PORT || 5000;

// Disable all caching
app.use((req, res, next) => {
  res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate, private, max-age=0');
  res.setHeader('Pragma', 'no-cache');
  res.setHeader('Expires', '0');
  next();
});

app.use(express.json());
app.use(express.static('.'));

// Serve trading interface
app.get('/trading', (req, res) => {
    res.sendFile(path.join(__dirname, 'trading.html'));
});

// API endpoint to get real-time HyperEVM token data
app.get('/api/tokens', async (req, res) => {
    try {
        console.log('📊 Fetching real-time HyperEVM token data...');
        // For Vercel, return mock data as Python scripts won't work
        const mockTokens = [
            { symbol: 'BUDDY', price: '0.01214000', change24h: '+2.45', volume: '1.2M' },
            { symbol: 'RUB', price: '0.00834521', change24h: '+1.23', volume: '856K' },
            { symbol: 'PURR', price: '0.00456789', change24h: '-0.87', volume: '2.1M' },
            { symbol: 'LHYPE', price: '0.02345678', change24h: '+5.67', volume: '3.4M' },
            { symbol: 'PiP', price: '0.00123456', change24h: '+0.12', volume: '678K' },
            { symbol: 'HSTR', price: '0.01876543', change24h: '+3.21', volume: '1.8M' },
            { symbol: 'KITTEN', price: '0.00987654', change24h: '-1.45', volume: '990K' },
            { symbol: 'HL', price: '0.00345678', change24h: '+2.78', volume: '1.5M' }
        ];
        res.json(mockTokens);
    } catch (error) {
        console.error('❌ Error fetching token data:', error);
        res.status(500).json({ error: 'Failed to fetch token data' });
    }
});

// API endpoint to get real-time order book
app.get('/api/orderbook/:symbol', (req, res) => {
    try {
        const symbol = req.params.symbol;
        console.log(`📈 Generating order book for ${symbol}...`);
        
        // Generate mock order book
        const orderbook = {
            bids: Array.from({length: 10}, (_, i) => ({
                price: (Math.random() * 0.001 + 0.01).toFixed(8),
                amount: (Math.random() * 1000 + 100).toFixed(2)
            })),
            asks: Array.from({length: 10}, (_, i) => ({
                price: (Math.random() * 0.001 + 0.011).toFixed(8),
                amount: (Math.random() * 1000 + 100).toFixed(2)
            }))
        };
        
        res.json(orderbook);
    } catch (error) {
        console.error('❌ Error generating orderbook:', error);
        res.status(500).json({ error: 'Failed to generate orderbook' });
    }
});

// Serve main page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

server.listen(PORT, '0.0.0.0', () => {
    console.log(`🚀 HyperEVM Trading Platform running on port ${PORT}`);
    console.log(`📱 Landing Page: http://localhost:${PORT}/`);
    console.log(`📊 Trading Interface: http://localhost:${PORT}/trading`);
});
