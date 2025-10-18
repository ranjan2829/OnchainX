# 🚀 OnchainX Authentication Setup Guide

## 📋 Prerequisites
- Supabase account (free tier available)
- Neon PostgreSQL account (free tier available)

## 🔧 Step 1: Set Up Supabase

1. **Create Supabase Project:**
   - Go to [supabase.com](https://supabase.com)
   - Sign up/Login and create a new project
   - Wait for project to be ready (2-3 minutes)

2. **Get Supabase Credentials:**
   - Go to Project Settings → API
   - Copy your:
     - **Project URL** (e.g., `https://xyz123.supabase.co`)
     - **Anon Key** (public key)
     - **Service Role Key** (secret key - keep this safe!)

3. **Configure Authentication:**
   - Go to Authentication → Settings
   - Enable Email authentication
   - Set Site URL to `http://localhost:3000` (for development)

## 🗄️ Step 2: Set Up Neon PostgreSQL

1. **Create Neon Database:**
   - Go to [neon.tech](https://neon.tech)
   - Sign up/Login and create a new project
   - Copy your connection string

2. **Connection String Format:**
   ```
   postgresql://username:password@host:port/database
   ```

## ⚙️ Step 3: Update Environment Variables

Edit `/backend/.env` file with your real credentials:

```env
# Supabase Configuration
SUPABASE_URL=https://your-actual-project-id.supabase.co
SUPABASE_ANON_KEY=your_actual_anon_key_here
SUPABASE_SERVICE_ROLE_KEY=your_actual_service_role_key_here

# Neon PostgreSQL Configuration
DATABASE_URL=postgresql://your_actual_username:your_actual_password@your_actual_host:5432/your_actual_database

# JWT Configuration (keep these)
JWT_SECRET_KEY=your-secret-key-change-this-in-production-very-long-and-random
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

# Application Configuration
APP_NAME=OnchainX
DEBUG=false
CORS_ORIGINS=http://localhost:3000,https://onchain-x.vercel.app
```

## 🚀 Step 4: Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

## 🗃️ Step 5: Create Database Tables

```bash
cd backend
python3 -c "from app.database import create_tables; create_tables(); print('Tables created!')"
```

## 🧪 Step 6: Test the System

1. **Start the server:**
   ```bash
   cd backend
   python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Test signup:**
   ```bash
   curl -X POST http://localhost:8000/auth/signup \
     -H "Content-Type: application/json" \
     -d '{"email":"test@example.com","password":"password123","username":"testuser","full_name":"Test User"}'
   ```

3. **Test signin:**
   ```bash
   curl -X POST http://localhost:8000/auth/signin \
     -H "Content-Type: application/json" \
     -d '{"email":"test@example.com","password":"password123"}'
   ```

## 📚 API Documentation

Once running, visit: `http://localhost:8000/docs`

## 🔒 Security Notes

- Never commit real credentials to git
- Use environment variables in production
- Rotate JWT secret keys regularly
- Enable HTTPS in production

## 🆘 Troubleshooting

**"Invalid API key" error:**
- Check your Supabase credentials are correct
- Ensure you're using the Service Role Key (not Anon Key) for backend

**Database connection errors:**
- Verify your Neon connection string
- Check if your IP is whitelisted in Neon

**Authentication errors:**
- Ensure email authentication is enabled in Supabase
- Check Site URL settings in Supabase Auth
