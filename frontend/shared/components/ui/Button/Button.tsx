import { ButtonProps } from './types';
import styles from './Button.module.scss';
import classNames from 'classnames';

export default function Button({
  children,
  textAlign = 'center',
  startIcon,
  endIcon,
  onClick,
  className,
}: ButtonProps) {
  return (
    <div className={styles.buttonContainer}>
      <button
        onClick={onClick}
        className={classNames(
          textAlign === 'start' ? styles.button_alignStart : '',
          textAlign === 'center' ? styles.button_alignCenter : '',
          textAlign === 'end' ? styles.button_alignEnd : ''
        )}
      >
        <>
          <div className={styles.start}>{startIcon}</div>
          <div>{children}</div>
          <div className={styles.end}>{endIcon}</div>
        </>
      </button>
    </div>
  );
}
