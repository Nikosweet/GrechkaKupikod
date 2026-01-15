import classes from '@/components/Auth.module.scss'

export default function Auth() {
  return (
    <form className={classes.form}>
        <label htmlFor="usernameLogin">Имя пользователя:</label>
        <input type="text" placeholder='Введите имя' name="usernameLogin" className={classes.input}/>
        <label htmlFor="passwordLogin">Пароль:</label>
        <input type="password" placeholder='Введите пароль' name="passwordLogin" className={classes.input}/>
        <button>Войти</button>
    </form>
  )
}
