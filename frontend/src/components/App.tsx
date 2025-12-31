import { Outlet } from 'react-router-dom'
import classes from './App.module.scss'
import myPng from '@/assets/my.png'
import Mouse from '@/assets/mouse.svg'
export default function App() {
  return (<>
    <div className={classes.App}>App</div>
    <Mouse />
    <img src={myPng} alt="" />
    <div>{myPng}</div>
    <Outlet/>
    </>
  )
}