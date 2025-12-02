import { ReactNode } from 'react';

export type ButtonProps = {
  children: ReactNode;
  textAlign?: 'start' | 'center' | 'end';
  startIcon?: ReactNode;
  endIcon?: ReactNode;
  onClick?: () => void;
  className?: string;
};
