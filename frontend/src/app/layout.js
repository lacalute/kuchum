import './globals.css'
import { Inter } from 'next/font/google'
import { Navigation } from '../../components/nav'
const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Kuchum Blog'
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div className='container'>
          <Navigation />
          {children}
        </div>
        </body>
    </html>
  )
}
