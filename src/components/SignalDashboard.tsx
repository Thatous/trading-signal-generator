import { useEffect, useState } from 'react';
import { fetchSignal } from '../services/api';

interface SignalDashboardProps {
  asset: string;
}

export function SignalDashboard({ asset }: SignalDashboardProps) {
  const [signal, setSignal] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const getSignal = async () => {
      try {
        setLoading(true);
        const data = await fetchSignal(asset);
        setSignal(data);
        setError('');
      } catch (err) {
        setError('Failed to fetch signal');
      } finally {
        setLoading(false);
      }
    };

    getSignal();
    const interval = setInterval(getSignal, 60000); // Update every minute

    return () => clearInterval(interval);
  }, [asset]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div className="text-red-500">{error}</div>;
  if (!signal) return null;

  return (
    <div className="bg-white rounded-lg shadow-lg p-6 mt-4">
      <h2 className="text-2xl font-semibold mb-4">Signal for {asset}</h2>
      <div className="grid grid-cols-2 gap-4">
        <div>
          <p className="text-gray-600">Signal</p>
          <p className={`text-xl font-bold ${signal.signal === 'BUY' ? 'text-green-600' : signal.signal === 'SELL' ? 'text-red-600' : 'text-yellow-600'}`}>
            {signal.signal}
          </p>
        </div>
        <div>
          <p className="text-gray-600">Price</p>
          <p className="text-xl font-bold">${signal.price.toFixed(2)}</p>
        </div>
        <div>
          <p className="text-gray-600">RSI</p>
          <p className="text-xl">{signal.rsi.toFixed(2)}</p>
        </div>
        <div>
          <p className="text-gray-600">MACD</p>
          <p className="text-xl">{signal.macd.toFixed(4)}</p>
        </div>
      </div>
    </div>
  );
}
