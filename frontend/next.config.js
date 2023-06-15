/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      {
        hostname: 'img2.teletype.in',
      },
    ],
  },
}

module.exports = nextConfig
