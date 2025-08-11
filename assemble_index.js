const fs = require('fs');
const path = require('path');

// This script combines the parts back into index.html for local development
try {
    const part1 = fs.readFileSync('index_part1.html', 'utf8');
    const part2 = fs.readFileSync('index_part2.html', 'utf8');
    const combined = part1 + part2;
    fs.writeFileSync('index.html', combined);
    console.log('✅ index.html assembled successfully');
} catch (error) {
    console.log('ℹ️ Parts not found, using existing index.html');
}
