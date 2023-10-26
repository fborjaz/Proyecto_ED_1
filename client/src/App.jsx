import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { TasksPage } from './pages/TasksPage'
import { TasksFormPage } from './pages/TasksFormPage'
import Home from './components/Home'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path = "/" element = {<Navigate to = "/shopping" />} />
        <Route path = "/shopping" element = {<Home />} />
        <Route path = "/shopping-create" element = {<TasksFormPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App