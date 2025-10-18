import React from 'react';
import { useAuth } from '../contexts/AuthContext';

const Dashboard: React.FC = () => {
  const { user, logout } = useAuth();

  const handleLogout = async () => {
    try {
      await logout();
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <h1>Welcome to OnchainX</h1>
        <button onClick={handleLogout} className="logout-button">
          Logout
        </button>
      </header>
      
      <div className="dashboard-content">
        <div className="user-info">
          <h2>User Information</h2>
          <div className="info-card">
            <p><strong>Email:</strong> {user?.email}</p>
            <p><strong>Username:</strong> {user?.username}</p>
            <p><strong>Full Name:</strong> {user?.full_name}</p>
            <p><strong>Status:</strong> {user?.is_active ? 'Active' : 'Inactive'}</p>
            <p><strong>Verified:</strong> {user?.is_verified ? 'Yes' : 'No'}</p>
            <p><strong>Member Since:</strong> {user?.created_at ? new Date(user.created_at).toLocaleDateString() : 'N/A'}</p>
          </div>
        </div>

        <div className="wallets-section">
          <h2>Connected Wallets</h2>
          {user?.wallets && user.wallets.length > 0 ? (
            <div className="wallets-list">
              {user.wallets.map((wallet) => (
                <div key={wallet.id} className="wallet-card">
                  <p><strong>Address:</strong> {wallet.address}</p>
                  <p><strong>Type:</strong> {wallet.wallet_type}</p>
                  <p><strong>Primary:</strong> {wallet.is_primary ? 'Yes' : 'No'}</p>
                </div>
              ))}
            </div>
          ) : (
            <div className="no-wallets">
              <p>No wallets connected yet.</p>
              <button className="connect-wallet-button">
                Connect Wallet
              </button>
            </div>
          )}
        </div>

        <div className="features-section">
          <h2>Features</h2>
          <div className="features-grid">
            <div className="feature-card">
              <h3>🔐 Secure Authentication</h3>
              <p>Your account is secured with Supabase authentication and JWT tokens.</p>
            </div>
            <div className="feature-card">
              <h3>💼 Wallet Integration</h3>
              <p>Connect your MetaMask or other Web3 wallets to manage your assets.</p>
            </div>
            <div className="feature-card">
              <h3>🌐 Onchain Operations</h3>
              <p>Perform secure blockchain transactions and interact with smart contracts.</p>
            </div>
            <div className="feature-card">
              <h3>📊 Analytics</h3>
              <p>Track your portfolio performance and transaction history.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
