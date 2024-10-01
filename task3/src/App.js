import React from 'react';
import PostForm from './components/PostForm';
import Posts from './components/Posts';

const App = () => {
  return (
    <div>
      <h1 style={{ textAlign: 'center' }}>Post App</h1>
      <PostForm />
      <Posts />
    </div>
  );
};

export default App;
