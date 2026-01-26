import classes from '@/components/Slider.module.scss'
import LeftArrow from '@/assets/slider/left-arrow.svg'
import RightArrow from '@/assets/slider/right-arrow.svg'
import SliderPhoto1 from '@/assets/slider/SliderPhoto1.jpg'
import SliderPhoto2 from '@/assets/slider/SliderPhoto2.jpg'
import { KeyboardEvent, useState } from 'react'

export default function Slider() {
    const [slide, setSlide] = useState(0);

    function handleLeftArrow() {
        if (slide === 0) return;
        setSlide(slide-1); 
    }

    function handleRightArrow() {
        if (slide === 1) return;
        setSlide(slide+1);
    }

    return (
        <div className={classes.sliderHolder}>
            <button className={classes.leftArrow} onClick={handleLeftArrow}>
                <LeftArrow width={30}></LeftArrow>
            </button>
            <div className={classes.slides} style={{transform: `translateX(${-slide*50}%)`}}>
                <img src={SliderPhoto1} alt="" className={classes.image} draggable="false"/>
                <img src={SliderPhoto2} alt="" className={classes.image} draggable="false"/>
            </div>
            <button className={classes.rightArrow} onClick={handleRightArrow}>
                <RightArrow width={30}></RightArrow>
            </button>
        </div>
    )
}
