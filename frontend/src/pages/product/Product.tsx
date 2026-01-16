import classes from './Product.module.scss'
export default function Product() {
  return (
    <>
        <div className={classes.wrapper}>
            <div className={classes.productHeader}></div>
            <ul className={classes.content}>
                <li className={classes.images}>
                    <img src="" alt="Фото продукта" />
                    <div className={classes.miniphotos}>
                        <img src="" alt="Другое фото 1" />
                        <img src="" alt="Другое фото 2" />
                        <img src="" alt="Другое фото 3" />
                        <img src="" alt="Другое фото 4" />
                    </div>
                </li>
                <li className={classes.params}>
                    <div className={classes.name}></div>
                    <div className={classes.reviews}></div>
                    <div className={classes.about}></div>
                </li>
                <li className={classes.order}>
                    <div className={classes.buy}></div>
                    <div className={classes.adress}></div>
                    <div className={classes.store}></div>
                </li>
            </ul>
            <div className={classes.recommend}>

            </div>
        </div>
    </>
  )
}
