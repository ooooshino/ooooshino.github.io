<script setup>
import avatar from '/avatar.png'
</script>

<template>
  <section>
    <div>
      <div>
        <img class="float-none lg:float-right
        w-24 h-24 
        sm:w-28 sm:h-28
        md:w-32 md:h-32
        lg:w-36 lg:h-36
        
        m-auto mb-10
        lg:m-6 lg:mb-0

        rounded-full " :src="avatar" alt="avatar" />
      </div>
      <h3 class="text-center sm:text-left ">ooooshino</h3>
      <ul>
        <li>1999 / 男 / 广东xx</li>
        <li>本科 / 广东东软学院计算机系 / 23届应届生</li>
        <li>技术博客：https://oshino.cc</li>
        <li>期望职位：web前端开发工程师</li>
        <li>手机：131-xxxx-xxxx（微信同号）</li>
        <li>邮箱：xxxx@gmail.com</li>
      </ul>
    </div>

  </section>
</template>
