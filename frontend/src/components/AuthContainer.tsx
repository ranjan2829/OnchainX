import React, { useState } from 'react';
import SigninForm from './SigninForm';
import SignupForm from './SignupForm';

const AuthContainer: React.FC = () => {
  const [isSignup, setIsSignup] = useState(false);

  return (
    <div className="auth-container">
      <div className="auth-wrapper">
        <div className="auth-header">
          <h1 className="brand-title">OnchainX</h1>
          <p className="brand-subtitle">Your Gateway to Web3</p>
        </div>
        
        {isSignup ? (
          <SignupForm onSwitchToSignin={() => setIsSignup(false)} />
        ) : (
          <SigninForm onSwitchToSignup={() => setIsSignup(true)} />
        )}
      </div>
    </div>
  );
};

export default AuthContainer;
