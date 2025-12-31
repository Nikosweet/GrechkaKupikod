import { Outlet } from 'react-router-dom'
import classes from './App.module.scss'
import myPng from '@/assets/my.png'
import Mouse from '@/assets/mouse.svg'
export default function App() {
  return (<>
    <div className={classes.App}>App123</div>
    <h1>PLATFORM={__PLATFORM__}</h1>
    <Mouse width={50} height={50} icon={true} className={classes.color} />
    <img src={myPng} alt="" />
    <div>{myPng}</div>
    <Outlet/>
    </>
  )
}