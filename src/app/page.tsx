import { useState } from 'react';
import { SignalDashboard } from '../components/SignalDashboard';
import { AssetSelector } from '../components/AssetSelector';

export default function Home() {
  const [selectedAsset, setSelectedAsset] = useState('AAPL');

  return (
    <main className="min-h-screen p-8">
      <h1 className="text-4xl font-bold mb-8">Trading Signal Generator</h1>
      <AssetSelector onSelect={setSelectedAsset} selected={selectedAsset} />
      <SignalDashboard asset={selectedAsset} />
    </main>
  );
}
