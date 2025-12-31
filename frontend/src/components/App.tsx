import { Outlet } from 'react-router-dom'
import classes from './App.module.scss'
import myPng from '@/assets/my.png'
export default function App() {
  return (<>
    <div className={classes.App}>App</div>
    <img src={myPng} alt="" />
    <div>{myPng}</div>
    <Outlet/>
    </>
  )
}