const ROOT_URL = "http://localhost:8000/";

export const AuthUrls = {
    LOGIN: `${ROOT_URL}tms/login/`,
    SIGNUP: `${ROOT_URL}tms/register/`,
    CHANGE_PASSWORD: `${ROOT_URL}tms/password/change/`,
    RESET_PASSWORD: `${ROOT_URL}tms/password/reset/`,
    RESET_PASSWORD_CONFIRM: `${ROOT_URL}tms/password/reset/confirm/`,
    USER_ACTIVATION: `${ROOT_URL}tms/registration/verify-email/`,
    USER_PROFILE: `${ROOT_URL}tms/user/`
};