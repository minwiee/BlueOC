import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { addPost } from '../redux/actions';

const PostForm = () => {
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');
  const dispatch = useDispatch();

  const handleSubmit = (e) => {
    e.preventDefault();
    const newPost = { title, body };
    dispatch(addPost(newPost));
    setTitle('');
    setBody('');
  };

  return (<>
    <h3 style={{ textAlign: 'center' }}>Share your thoughts</h3>
    <form onSubmit={handleSubmit} style={{ 
      display: 'flex', 
      flexDirection: 'column', 
      margin: '0 auto',
      gap: '1rem', width: '60%',
      padding: '1rem',    
      backgroundColor: '#f9f9f9',
      borderRadius: '10px',
      boxShadow: '0 4px 10px rgba(0, 0, 0, 0.1)' }}>
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        required
        style={{ padding: '0.75rem', fontSize: '1rem', borderRadius: '5px', border: '1px solid #ccc' }}
      />
      <textarea
        placeholder="Body"
        value={body}
        onChange={(e) => setBody(e.target.value)}
        required
        style={{ padding: '0.75rem', fontSize: '1rem', borderRadius: '5px', border: '1px solid #ccc', resize: 'none' }}
      />
      <button type="submit" style={{ padding: '0.75rem', backgroundColor: '#007bff', color: '#fff', border: 'none', borderRadius: '5px', cursor: 'pointer', fontSize: '1rem' }}>
        Add Post
      </button>
    </form>
    </>
  );
};

export default PostForm;
