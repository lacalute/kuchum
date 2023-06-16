"use client"
import {Search} from "@/app/components/UI/search/Search";
import {useEffect, useState} from "react";
import './feed.scss'
import {Post} from "@/app/components/post/Post";
import {useFetching} from "@/app/hooks/useFetching";
import {PostService} from "@/app/service/posts.service";


export default function MyFeed() {
  const [inputValue, setInputValue] = useState('')
  const {data: feedPosts, error, isLoading, fetching: fetchPosts} =  useFetching()

  useEffect(() => {
    fetchPosts(() => PostService.getMyFeed())
  }, [])

  return (
      <section className='feed'>
        <h1 className='feed__title'>Моя лента <span>(1)</span></h1>
        <Search value={inputValue} onChange={setInputValue} />

        <div className="feed__list">
          {feedPosts?.data.map(post => {
            return (
                <Post {...post} key={post.id} />
            )
          })}
        </div>
      </section>
  )
}

