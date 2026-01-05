import classes from '@/pages/shop/Shop.module.scss'
import Card from '@/components/Card'
export default function Shop() {
  return (
    <>
      <div className={classes.sliderHolder}>It's not ready right now</div>
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
