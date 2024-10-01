import { FETCH_POSTS, ADD_POST } from './actions';

const initialState = {
  posts: []
};

const rootReducer = (state = initialState, action) => {
  switch (action.type) {
    case FETCH_POSTS:
      return { ...state, posts: action.payload };
    case ADD_POST:
      return { ...state, posts: [action.payload, ...state.posts] };
    default:
      return state;
  }
};

export default rootReducer;
