# Use Node.js image for building
FROM node:18-alpine AS build

# Set the NODE_OPTIONS to allow legacy OpenSSL algorithms
ENV NODE_OPTIONS=--openssl-legacy-provider

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package.json package-lock.json ./
RUN npm install  # Install dependencies

# Copy the rest of the frontend files
COPY . . 

# Build the frontend for production
RUN npm run build

# Use Nginx to serve the frontend
FROM nginx:alpine

# Copy the built files to Nginx's default directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 for serving the frontend
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
