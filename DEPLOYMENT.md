# Deployment Guide

## Quick GitHub & Vercel Deployment

### Step 1: Upload to GitHub

1. **Create a new GitHub repository** (public or private)
2. **Clone this Replit to your local machine** or download the files:
   - `index.html` (main trading interface)
   - `server.js` (Node.js server)
   - `package.json` (dependencies)  
   - `vercel.json` (Vercel configuration)
   - `README.md` (project documentation)
   - `DEPLOYMENT.md` (this file)

3. **Initialize git and push to GitHub:**
```bash
git init
git add .
git commit -m "Initial commit: HyperEVM Trading Platform"
git branch -M main
git remote add origin https://github.com/yourusername/hyperevm-trading-platform.git
git push -u origin main
```

### Step 2: Deploy to Vercel

1. **Go to [vercel.com](https://vercel.com)** and sign in with GitHub
2. **Import your repository:**
   - Click "New Project"
   - Select your `hyperevm-trading-platform` repository
   - Click "Import"

3. **Configure deployment settings:**
   - Framework Preset: **Other**
   - Build Command: `npm install` (leave default)
   - Output Directory: Leave empty
   - Install Command: `npm install`

4. **Deploy:**
   - Click "Deploy"
   - Wait for deployment to complete (~1-2 minutes)
   - Your app will be live at `https://your-project-name.vercel.app`

### Step 3: Test the Deployment

1. **Visit your live URL**
2. **Connect your MetaMask wallet**
3. **Switch to HyperEVM network (Chain ID: 999)**
4. **Test the EIP-712 signing by clicking Long**

## Key Files for Deployment

### Required Files:
- `index.html` - Main trading interface
- `server.js` - Express server
- `package.json` - Dependencies configuration
- `vercel.json` - Vercel deployment settings

### Optional Files:
- `README.md` - Project documentation
- `DEPLOYMENT.md` - This deployment guide
- `.gitignore` - Git ignore rules

## Environment Variables

No environment variables are required for basic functionality. The platform:
- Connects directly to HyperEVM blockchain
- Uses public APIs (DexScreener, Gecko Terminal)
- Operates with client-side wallet connections

## Troubleshooting

### Build Issues:
- Ensure `package.json` has correct dependencies
- Check that `vercel.json` is properly configured
- Verify all file paths are correct

### Runtime Issues:
- Check browser console for JavaScript errors
- Ensure MetaMask is installed and connected
- Verify HyperEVM network is added to MetaMask

### Trading Issues:
- Confirm wallet has HYPE tokens
- Check network connectivity
- Verify contract addresses are correct

## Post-Deployment Checklist

- [ ] App loads without errors
- [ ] Real-time price feeds working
- [ ] Wallet connection functional
- [ ] EIP-712 signing prompts appear
- [ ] Trading executes successfully
- [ ] Position tracking works

## Support

For deployment issues:
- Check Vercel deployment logs
- Review browser developer console
- Verify all dependencies are installed

Your HyperEVM Trading Platform is now live and ready for trading!