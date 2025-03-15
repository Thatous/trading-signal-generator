interface AssetSelectorProps {
  onSelect: (asset: string) => void;
  selected: string;
}

const ASSETS = [
  'AAPL',
  'GOOGL',
  'MSFT',
  'TSLA',
  'AMZN',
  'EURUSD',
  'GBPUSD',
  'USDJPY'
];

export function AssetSelector({ onSelect, selected }: AssetSelectorProps) {
  return (
    <div className="flex gap-2 flex-wrap">
      {ASSETS.map(asset => (
        <button
          key={asset}
          onClick={() => onSelect(asset)}
          className={`px-4 py-2 rounded ${selected === asset ? 'bg-blue-600 text-white' : 'bg-gray-200 hover:bg-gray-300'}`}
        >
          {asset}
        </button>
      ))}
    </div>
  );
}
