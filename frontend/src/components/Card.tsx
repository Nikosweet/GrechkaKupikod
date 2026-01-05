import classes from '@/components/Card.module.scss'
import Star from '@/assets/cardImg/star.svg'
import Review from '@/assets/cardImg/review.svg'
import GolfClub from '@/assets/cardImg/golfclub.jpg'
export default function() {
    return (
        <li className={classes.Card}>
            <a href='#'><img src={GolfClub} alt="" className={classes.image}/></a>
            <div className={classes.price}>144 ₽</div>
            <div className={classes.name}>Клюшка для гольфа</div>
            <div className={classes.gradenreview}>
                <Star width={17} height={17} fill={'yellow'} className={classes.star}/>
                <div className={classes.grade}>4.78</div>
                <Review width={17} height={17} fill={'rgb(158, 154, 154)'} className={classes.review}/>
                <div className={classes.reviews}>14378</div>
            </div>
        </li>
    )
} 
