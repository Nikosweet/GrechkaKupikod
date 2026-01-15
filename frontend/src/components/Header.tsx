
import classes from '@/components/Header.module.scss'
import Basket from '@/assets/header/basket.svg'
import Profile from '@/assets/header/profile.svg'
import Box from '@/assets/header/box.svg'
import Catalog from '@/assets/header/catalog.svg'
import Search from '@/assets/header/search.svg'
import Auth from '@/components/Auth'

import { useState } from 'react'

export default function Header() {
  const ISAUTHORIZED = false;
  const [authComponent, setAuthComponent] = useState(<></>)

  function AuthFormRender() {
    setAuthComponent(Auth);
  }
  function RegisterFormRender() {

  }
  return (
    <>
    <header className={classes.header}>
        <ul className={classes.headerList}>
          <li><ul className={classes.content}>
          <li><a href="#"><h1 className={classes.logo}>Grechka</h1></a></li>
          <li><button className={classes.catalog}>Каталог <Catalog width={23}/></button></li>
          <li>
            <form className={classes.form} action="">
              <input type="text" name="" id="" className={classes.search} placeholder='Введите товар...'/>
              <button type='submit' className={classes.searchbutton}><Search width={20}/></button>
            </form>
          </li>
          </ul></li>
          { ISAUTHORIZED ? (
            <li>
              <ul className={classes.icons}>            
                <li><a href='#' className={classes.profile}><Profile width={28}/></a></li>
                <li><a href="#" ><Basket width={35} /></a></li>
                <li><a href='#' className={classes.orders}><Box width={33}/></a></li>
              </ul>
            </li>
          ) : (
            <li>
              <ul className={classes.icons}>
                <li><button className={classes.authButton} onClick={AuthFormRender}>Войти</button></li>
                <li><button className={classes.authButton} onClick={RegisterFormRender}>Зарегистрироваться</button></li>
              </ul>
            </li>
          )
          }
    
        </ul>
    </header>
    {authComponent}
    </>
  )
}
