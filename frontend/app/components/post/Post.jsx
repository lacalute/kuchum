import Image from 'next/image'
import './post.scss'
import {useEffect} from "react";
import {AiOutlineEye} from "react-icons/ai";
import {CiFaceSmile} from "react-icons/ci";
import {BiCommentDetail} from "react-icons/bi";

export const Post = ({author, title, body, date, views, comments, action}) => {
  const heightOfPost = () => {
    let h = 4
    const length = body.length
    console.log(length)

    if (length >= 40 && length <= 70) {
      h = 6
    } else if (length > 70 && length < 90) {
      h = 7
    } else if (length > 90 && length < 170) {
      h = 8
    } else if (length > 170) {
      h = 9
    }
    return `span ${h}`
  }

  useEffect(() => {
    heightOfPost()
  }, [body])

  return (
      <article style={{gridRowEnd: heightOfPost()}} className='post'>
        <div className="post__author">
          <div className='post__author-img'>
            <Image
                src={author?.avatar}
                width={100}
                height={100}
                alt="author avatar"
            />
          </div>
          <div className='post__author-info'>
            <div className="post__author-name">{author?.name}</div>
            <div className="post__author-username">{author?.userName}</div>
          </div>

          <div className="post__date">{date}</div>
        </div>

        <div className="post__title">{title}</div>
        <div className="post__body">{body}</div>

        <div className="post__footer">
          <button className='post__btn'>
            <AiOutlineEye size={18} />
            {views}
          </button>
          <button className='post__btn'>
            <BiCommentDetail size={18} />
            {comments}
          </button>
          <button className='post__btn'>
            <CiFaceSmile size={18} />
            {action}
          </button>
        </div>
      </article>
  )
}