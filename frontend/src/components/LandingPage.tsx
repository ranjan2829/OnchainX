import React from 'react';
import { useAuth } from '../contexts/AuthContext';
import AuthContainer from './AuthContainer';
import Dashboard from './Dashboard';

const LandingPage: React.FC = () => {
  const { isAuthenticated, loading } = useAuth();

  if (loading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading...</p>
      </div>
    );
  }

  if (isAuthenticated) {
    return <Dashboard />;
  }

  return (
    <div className="landing-page">
      {/* Hero Section */}
      <section className="hero">
        <div className="hero-content">
          <div className="hero-text">
            <h1 className="hero-title">
              <span className="terminal-prompt">$</span> OnchainX
            </h1>
            <p className="hero-subtitle">
              The future of decentralized authentication
            </p>
            <p className="hero-description">
              Secure, fast, and reliable authentication system built for the Web3 era. 
              Connect your wallet, manage your identity, and access the decentralized future.
            </p>
            <div className="hero-features">
              <div className="feature-item">
                <span className="feature-icon">🔐</span>
                <span>Secure Authentication</span>
              </div>
              <div className="feature-item">
                <span className="feature-icon">⚡</span>
                <span>Lightning Fast</span>
              </div>
              <div className="feature-item">
                <span className="feature-icon">🌐</span>
                <span>Web3 Ready</span>
              </div>
            </div>
          </div>
          <div className="hero-auth">
            <AuthContainer />
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="features">
        <div className="container">
          <h2 className="section-title">
            <span className="terminal-prompt">{'>'}</span> Why Choose OnchainX?
          </h2>
          <div className="features-grid">
            <div className="feature-card">
              <div className="feature-header">
                <span className="feature-icon">🛡️</span>
                <h3>Enterprise Security</h3>
              </div>
              <p>
                Built with industry-standard security practices. Your data is protected 
                with end-to-end encryption and secure authentication protocols.
              </p>
            </div>
            <div className="feature-card">
              <div className="feature-header">
                <span className="feature-icon">🔗</span>
                <h3>Wallet Integration</h3>
              </div>
              <p>
                Seamlessly connect with MetaMask, WalletConnect, and other popular 
                Web3 wallets. Your keys, your control.
              </p>
            </div>
            <div className="feature-card">
              <div className="feature-header">
                <span className="feature-icon">⚡</span>
                <h3>Lightning Performance</h3>
              </div>
              <p>
                Optimized for speed and reliability. Experience sub-second authentication 
                and instant access to your decentralized applications.
              </p>
            </div>
            <div className="feature-card">
              <div className="feature-header">
                <span className="feature-icon">🌍</span>
                <h3>Global Scale</h3>
              </div>
              <p>
                Deployed on a global infrastructure with 99.9% uptime. Access your 
                account from anywhere in the world, anytime.
              </p>
            </div>
            <div className="feature-card">
              <div className="feature-header">
                <span className="feature-icon">🔧</span>
                <h3>Developer Friendly</h3>
              </div>
              <p>
                Comprehensive APIs and SDKs for easy integration. Build amazing 
                applications with our robust authentication infrastructure.
              </p>
            </div>
            <div className="feature-card">
              <div className="feature-header">
                <span className="feature-icon">📊</span>
                <h3>Analytics Dashboard</h3>
              </div>
              <p>
                Track your authentication metrics, monitor security events, and 
                gain insights into your account activity.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Tech Stack Section */}
      <section className="tech-stack">
        <div className="container">
          <h2 className="section-title">
            <span className="terminal-prompt">{'>'}</span> Built with Modern Technology
          </h2>
          <div className="tech-grid">
            <div className="tech-item">
              <div className="tech-icon">⚛️</div>
              <span>React</span>
            </div>
            <div className="tech-item">
              <div className="tech-icon">🐍</div>
              <span>FastAPI</span>
            </div>
            <div className="tech-item">
              <div className="tech-icon">🐘</div>
              <span>PostgreSQL</span>
            </div>
            <div className="tech-item">
              <div className="tech-icon">🔐</div>
              <span>Supabase</span>
            </div>
            <div className="tech-item">
              <div className="tech-icon">☁️</div>
              <span>Neon</span>
            </div>
            <div className="tech-item">
              <div className="tech-icon">🚀</div>
              <span>Render</span>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="cta">
        <div className="container">
          <div className="cta-content">
            <h2>Ready to Get Started?</h2>
            <p>Join thousands of users who trust OnchainX for their authentication needs.</p>
            <div className="cta-stats">
              <div className="stat">
                <span className="stat-number">10K+</span>
                <span className="stat-label">Active Users</span>
              </div>
              <div className="stat">
                <span className="stat-number">99.9%</span>
                <span className="stat-label">Uptime</span>
              </div>
              <div className="stat">
                <span className="stat-number">50+</span>
                <span className="stat-label">Integrations</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="footer">
        <div className="container">
          <div className="footer-content">
            <div className="footer-section">
              <h3>OnchainX</h3>
              <p>The future of decentralized authentication</p>
            </div>
            <div className="footer-section">
              <h4>Product</h4>
              <ul>
                <li><a href="#features">Features</a></li>
                <li><a href="#security">Security</a></li>
                <li><a href="#pricing">Pricing</a></li>
                <li><a href="#docs">Documentation</a></li>
              </ul>
            </div>
            <div className="footer-section">
              <h4>Company</h4>
              <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#blog">Blog</a></li>
                <li><a href="#careers">Careers</a></li>
                <li><a href="#contact">Contact</a></li>
              </ul>
            </div>
            <div className="footer-section">
              <h4>Support</h4>
              <ul>
                <li><a href="#help">Help Center</a></li>
                <li><a href="#status">Status</a></li>
                <li><a href="#privacy">Privacy</a></li>
                <li><a href="#terms">Terms</a></li>
              </ul>
            </div>
          </div>
          <div className="footer-bottom">
            <p>&copy; 2024 OnchainX. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LandingPage;
