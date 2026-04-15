import React, { useEffect, useState } from 'react'

export function App() {
  const [health, setHealth] = useState('checking')

  useEffect(() => {
    fetch('http://localhost:8000/health')
      .then((res) => res.json())
      .then((data) => setHealth(data.status))
      .catch(() => setHealth('offline'))
  }, [])

  return (
    <main style={{ fontFamily: 'sans-serif', margin: '2rem', maxWidth: 900 }}>
      <h1>Mobile Flow Mapper</h1>
      <p>API health: <strong>{health}</strong></p>
      <section style={{ border: '1px solid #ddd', borderRadius: 8, padding: 16 }}>
        <h2>Viewer Scaffold</h2>
        <ul>
          <li>Graph panel placeholder</li>
          <li>Screenshot panel placeholder</li>
          <li>Hotspot overlays placeholder</li>
        </ul>
      </section>
    </main>
  )
}
