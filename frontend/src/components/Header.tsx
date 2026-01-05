import classes from '@/components/Header.module.scss'
import Basket from '@/assets/header/basket.svg'
import Profile from '@/assets/header/profile.svg'
import Box from '@/assets/header/box.svg'
export default function Header() {
  return (
    <header className={classes.header}>
        <ul className={classes.headerList}>
          <li><a href="#"><h1 className={classes.logo}>Grechka</h1></a></li>
          <li><button className={classes.catalog}>Каталог</button></li>
          <li><input type="text" name="" id="" className={classes.search} placeholder='Введите товар...'/></li>
          <li>
            <ul className={classes.icons}>            
              <a href='#' className={classes.profile}><Profile width={28}/></a>
              <a href="" ><Basket width={35} /></a>
              <a className={classes.orders}><Box width={33}/></a>
            </ul>
          </li>
    
        </ul>
    </header>
  )
}
