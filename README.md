# HyperEVM Real-Time Trading Platform

A cutting-edge blockchain trading platform delivering hyper-responsive real-time token interactions with advanced market data aggregation and intelligent trading features.

## 🚀 Features

- **Real-Time Trading**: Live HyperEVM token data from DexScreener and Gecko Terminal
- **Mobile-First Design**: Optimized for touch interactions on mobile devices
- **Advanced Order Book**: Real-time buy/sell percentages with dynamic updates
- **Professional Charts**: TradingView-style candlestick charts with live data
- **Wallet Integration**: MetaMask connection with HyperEVM mainnet support
- **Authentic Data**: Real tokens from HyperSwap, Project X, Kittenswap DEXs
- **Live Market Data**: Real funding rates, price feeds, and trading volumes

## 🌐 Live Demo

Deploy this project instantly on Vercel:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Backpacksasa/Backpacksasa)

## 🛠️ Technology Stack

- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Node.js with Express.js
- **Real-Time**: Socket.IO for live data streaming
- **Blockchain**: Ethers.js v6 for HyperEVM integration
- **Data Sources**: DexScreener API, Gecko Terminal API
- **Styling**: Mobile-first responsive design with dark theme

## 📱 Supported Tokens

- **BUDDY** - Real HyperEVM token with live pricing
- **RUB** - Connected to Project X DEX
- **PURR** - Kittenswap integration
- **LHYPE** - HyperSwap pool data
- **PiP** - Live market data
- **HSTR** - Real trading volume
- **KITTEN** - Authentic DEX data
- **HL** - Live price feeds
- **LIQD** - Real-time updates
- **VEGAS** - Market integration

## ⚡ Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Backpacksasa/Backpacksasa.git
   cd Backpacksasa
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

### Vercel Deployment

1. **Import from GitHub**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import this repository

2. **Configure Settings**
   - Framework Preset: Other
   - Build Command: `npm install`
   - Output Directory: Leave empty
   - Install Command: `npm install`

3. **Deploy**
   - Click "Deploy"
   - Your trading platform will be live in minutes!

## 🔧 Configuration

### Environment Variables

No environment variables required for basic functionality. The platform connects to public APIs and HyperEVM mainnet.

### Vercel Configuration

The project includes a pre-configured `vercel.json`:

```json
{
  "version": 2,
  "name": "hyperevm-trading-platform",
  "builds": [
    {
      "src": "server.js",
      "use": "@vercel/node"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/server.js"
    }
  ],
  "env": {
    "NODE_ENV": "production"
  }
}
```

## 📊 API Endpoints

- `GET /api/tokens` - Real-time HyperEVM token data
- `GET /api/orderbook/:symbol` - Live order book for specific token
- `GET /api/chart/:symbol` - Real-time chart data
- `GET /` - Trading interface

## 🔗 Blockchain Integration

- **Network**: HyperEVM Mainnet (Chain ID: 999)
- **Wallet**: MetaMask integration with automatic network switching
- **Tokens**: Real HYPE token transfers for position opening
- **Security**: EIP-712 message signing for trade verification

## 📱 Mobile Optimization

- **Viewport**: Optimized for 375px mobile screens
- **Touch**: Disabled text selection and tap highlights
- **Performance**: Lightweight vanilla JavaScript for fast loading
- **UX**: Native app-like experience with smooth interactions

## 🎨 Design Features

- **Dark Theme**: Professional black background with white text
- **Real-Time Updates**: Live price changes with color coding
- **Responsive Layout**: Flexbox-based mobile-first design
- **Professional Charts**: TradingView-style visualization
- **Smooth Animations**: Enhanced user experience

## 🔒 Security

- **No API Keys Required**: Uses public blockchain data
- **Client-Side Only**: No sensitive data stored on servers
- **Wallet Integration**: Secure MetaMask connection
- **Real Transactions**: Authentic blockchain interactions

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the ISC License.

## 🆘 Support

If you encounter any issues:

1. Check the [Issues](https://github.com/Backpacksasa/Backpacksasa/issues) page
2. Create a new issue with detailed description
3. Include browser console logs if applicable

## 🌟 Star this Repository

If you find this project useful, please give it a star! ⭐

---

**Built with ❤️ for the HyperEVM ecosystem**