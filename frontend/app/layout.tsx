import type { Metadata } from 'next';
import '../styles/globals.scss';
import { LayoutProps } from './types';

export const metadata: Metadata = {
  title: 'BAP',
  description: 'Business analytics platform ',
};

export default function RootLayout({ children }: LayoutProps) {
  return (
    <html lang="ru">
      <body>{children}</body>
    </html>
  );
}
