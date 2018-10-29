export default function(state = {}, action) {
    switch(action.type) {
        case "LOGIN_SUCCESS":
            return { ...state, login:action.payload};
        case "LOGOUT_SUCCESS":
            return { ...state, login:null};
        default:
            return state;
    }
}