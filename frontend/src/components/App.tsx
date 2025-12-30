import { Outlet } from 'react-router-dom'
import classes from './App.module.scss'
export default function App() {
  return (<>
    <div className={classes.App}>App</div>
    <Outlet/>
    </>
  )
}