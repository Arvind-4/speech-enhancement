import type { Metadata } from 'next';
import Script from 'next/script';

import '@src/app/globals.css';
import Header from '@src/components/ui/header';

export const metadata: Metadata = {
  title: 'Speech Enhancement',
  description: 'A web app to enhance speech',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Header />
        <div className="min-h-screen">{children}</div>
        <Script
          src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.2.1/flowbite.min.js"
          strategy="beforeInteractive"
        ></Script>
      </body>
    </html>
  );
}
