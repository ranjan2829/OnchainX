# 🚀 OnchainX Deployment Guide for Render

## 📋 Prerequisites
- Render account (free tier available)
- Supabase project with credentials
- Neon PostgreSQL database

## 🔧 Step 1: Set Up Environment Variables in Render

### In your Render Dashboard:

1. **Go to your Web Service**
2. **Navigate to Environment tab**
3. **Add the following environment variables:**

```env
# Supabase Configuration
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_ANON_KEY=your_supabase_anon_key_here
SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key_here

# Neon PostgreSQL Configuration
DATABASE_URL=postgresql://username:password@host:port/database

# JWT Configuration
JWT_SECRET_KEY=your_jwt_secret_key_here_make_it_long_and_random

# Application Configuration
APP_NAME=OnchainX
DEBUG=false
CORS_ORIGINS=https://your-frontend-domain.vercel.app
```

## 🔑 Step 2: Get Your Credentials

### Supabase Credentials:
1. Go to your Supabase project dashboard
2. Navigate to **Settings** → **API**
3. Copy:
   - **Project URL** (e.g., `https://xyz123.supabase.co`)
   - **Anon Key** (public key)
   - **Service Role Key** (secret key)

### Neon PostgreSQL:
1. Go to your Neon dashboard
2. Copy your connection string
3. Format: `postgresql://username:password@host:port/database`

### JWT Secret Key:
Generate a secure random string:
```bash
# Option 1: Using Python
python -c "import secrets; print(secrets.token_urlsafe(32))"

# Option 2: Using OpenSSL
openssl rand -base64 32
```

## 🚀 Step 3: Deploy to Render

### Backend Deployment:
1. **Connect your GitHub repository to Render**
2. **Create a new Web Service**
3. **Configure the service:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Environment:** Python 3
4. **Add all environment variables from Step 1**
5. **Deploy!**

### Frontend Deployment (Vercel):
1. **Connect your GitHub repository to Vercel**
2. **Configure build settings:**
   - **Framework Preset:** Create React App
   - **Root Directory:** `frontend`
   - **Build Command:** `npm run build`
   - **Output Directory:** `build`
3. **Add environment variable:**
   - `REACT_APP_API_URL` = `https://your-render-backend-url.onrender.com`
4. **Deploy!**

## 🔧 Step 4: Update CORS Settings

After deployment, update your backend CORS origins:

1. **In Render Environment Variables:**
   ```env
   CORS_ORIGINS=https://your-frontend-domain.vercel.app
   ```

2. **Redeploy your backend**

## 🧪 Step 5: Test Your Deployment

### Test Backend:
```bash
curl https://your-backend-url.onrender.com/
# Should return: {"message":"Hello World !"}
```

### Test Frontend:
1. Visit your Vercel URL
2. Try signing up with a new account
3. Test the authentication flow

## 🆘 Troubleshooting

### Common Issues:

**1. Environment Variables Not Set:**
- Double-check all variables are added in Render
- Ensure no typos in variable names
- Redeploy after adding variables

**2. Database Connection Issues:**
- Verify your Neon connection string
- Check if your IP is whitelisted in Neon
- Ensure database is active

**3. Supabase Authentication Errors:**
- Verify your Supabase credentials
- Check if email authentication is enabled
- Ensure Site URL is set correctly in Supabase

**4. CORS Issues:**
- Update CORS_ORIGINS with your frontend URL
- Redeploy backend after CORS changes

### Debug Commands:

**Check Environment Variables:**
```bash
# Add this to your backend temporarily
import os
print("Environment variables:")
for key, value in os.environ.items():
    if any(x in key.upper() for x in ['SUPABASE', 'DATABASE', 'JWT']):
        print(f"{key}: {value[:10]}..." if len(value) > 10 else f"{key}: {value}")
```

## 📚 Additional Resources

- [Render Documentation](https://render.com/docs)
- [Vercel Documentation](https://vercel.com/docs)
- [Supabase Documentation](https://supabase.com/docs)
- [Neon Documentation](https://neon.tech/docs)

## 🎉 Success!

Once deployed, your full-stack authentication system will be live and accessible to users worldwide!

**Backend URL:** `https://your-backend.onrender.com`
**Frontend URL:** `https://your-frontend.vercel.app`
**API Documentation:** `https://your-backend.onrender.com/docs`
