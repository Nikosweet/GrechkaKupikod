import classes from '@/components/Auth.module.scss'
import { MouseEventHandler } from 'react';

type Props = {
  isRegister: boolean;
  close: MouseEventHandler;
}

export default function Auth(props: Props) {
  const {isRegister, close} = props;
  console.log(isRegister)
  return (
    <form className={classes.form}>
        <button className={classes.close} type='button' onClick={close}>X</button>
        <label htmlFor="usernameLogin">Имя пользователя:</label>
        <input type="text" placeholder='Введите имя' name="usernameLogin" className={classes.input}/>
        <label htmlFor="passwordLogin">Пароль:</label>
        <input type="password" placeholder='Введите пароль' name="passwordLogin" className={classes.input}/>
        { isRegister ? (<button className={classes.button}>Зарегистрироваться</button>) : (<button className={classes.button}>Войти</button>) }
    </form>
  )
}
