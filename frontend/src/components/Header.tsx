import classes from '@/components/Header.module.scss'
import Basket from '@/assets/header/basket.svg'
import Profile from '@/assets/header/profile.svg'
import Box from '@/assets/header/box.svg'
import Catalog from '@/assets/header/catalog.svg'
import Search from '@/assets/header/search.svg'
export default function Header() {
  return (
    <header className={classes.header}>
        <ul className={classes.headerList}>
          <li><ul className={classes.content}>
          <li><a href="#"><h1 className={classes.logo}>Grechka</h1></a></li>
          <li><button className={classes.catalog}>Каталог <Catalog width={23}/></button></li>
          <li>
            <form className={classes.form} action="">
              <input type="text" name="" id="" className={classes.search} placeholder='Введите товар...'/>
              <button type='submit' className={classes.button}><Search width={20}/></button>
            </form>
          </li>
          </ul></li>
          <li>
            <ul className={classes.icons}>            
              <a href='#' className={classes.profile}><Profile width={28}/></a>
              <a href="#" ><Basket width={35} /></a>
              <a href='#' className={classes.orders}><Box width={33}/></a>
            </ul>
          </li>
    
        </ul>
    </header>
  )
}
