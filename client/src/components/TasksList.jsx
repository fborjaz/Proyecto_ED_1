import { useEffect } from "react";

export function TasksList() {

    useEffect(()=> {
        console.log('Page loader')
    },[])

  return (
    <div>TasksList</div>
  )
}

export default TasksList