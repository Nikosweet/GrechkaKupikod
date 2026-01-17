import classes from '@/pages/shop/Shop.module.scss'
import Slider from '@/components/Slider'
import Card from '@/components/Card'
export default function Shop() {
  return (
    <>
      <Slider></Slider>
      <ul className={classes.Cardholder}>
        <Card></Card>
        <Card></Card>
        <Card></Card>
        <Card></Card>
        <Card></Card>
        <Card></Card>
        <Card></Card>
        <Card></Card>
        <Card></Card>
        <Card></Card>
      </ul>
    </>
  )
}
