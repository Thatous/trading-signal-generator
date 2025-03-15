const API_BASE_URL = 'http://localhost:8000';

export async function fetchSignal(asset: string) {
  const response = await fetch(`${API_BASE_URL}/signals/${asset}`);
  if (!response.ok) {
    throw new Error('Failed to fetch signal');
  }
  return response.json();
}

export async function runBacktest(asset: string, startDate: string, endDate: string) {
  const response = await fetch(`${API_BASE_URL}/backtest`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ asset, start_date: startDate, end_date: endDate }),
  });
  if (!response.ok) {
    throw new Error('Failed to run backtest');
  }
  return response.json();
}
