import { RisksProps } from './types';
import styles from './RiskPage.module.scss';

export default function RisksPage({ children }: RisksProps) {
  return (
    <div className={styles.wrapper}>
      <div className={styles.wrapper_content}></div>

      {children}
    </div>
  );
}
