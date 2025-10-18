import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export interface User {
  id: number;
  email: string;
  username: string;
  full_name: string;
  supabase_id: string;
  is_active: boolean;
  is_verified: boolean;
  created_at: string;
  wallets: Wallet[];
}

export interface Wallet {
  id: number;
  address: string;
  wallet_type: string;
  is_primary: boolean;
  created_at: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
  user: User;
}

export interface SignupData {
  email: string;
  password: string;
  username: string;
  full_name: string;
}

export interface SigninData {
  email: string;
  password: string;
}

class AuthService {
  private token: string | null = null;

  constructor() {
    this.token = localStorage.getItem('access_token');
  }

  setToken(token: string) {
    this.token = token;
    localStorage.setItem('access_token', token);
  }

  getToken(): string | null {
    return this.token || localStorage.getItem('access_token');
  }

  clearToken() {
    this.token = null;
    localStorage.removeItem('access_token');
  }

  getAuthHeaders() {
    const token = this.getToken();
    return token ? { Authorization: `Bearer ${token}` } : {};
  }

  async signup(data: SignupData): Promise<AuthResponse> {
    try {
      const response = await axios.post(`${API_URL}/auth/signup`, data);
      const authData = response.data;
      this.setToken(authData.access_token);
      return authData;
    } catch (error: any) {
      throw new Error(error.response?.data?.detail || 'Signup failed');
    }
  }

  async signin(data: SigninData): Promise<AuthResponse> {
    try {
      const response = await axios.post(`${API_URL}/auth/signin`, data);
      const authData = response.data;
      this.setToken(authData.access_token);
      return authData;
    } catch (error: any) {
      throw new Error(error.response?.data?.detail || 'Signin failed');
    }
  }

  async logout(): Promise<void> {
    try {
      await axios.post(`${API_URL}/auth/logout`, {}, {
        headers: this.getAuthHeaders()
      });
    } catch (error) {
      console.error('Logout error:', error);
    } finally {
      this.clearToken();
    }
  }

  async getCurrentUser(): Promise<User> {
    try {
      const response = await axios.get(`${API_URL}/auth/me`, {
        headers: this.getAuthHeaders()
      });
      return response.data;
    } catch (error: any) {
      throw new Error(error.response?.data?.detail || 'Failed to get user data');
    }
  }

  isAuthenticated(): boolean {
    return !!this.getToken();
  }
}

export const authService = new AuthService();
