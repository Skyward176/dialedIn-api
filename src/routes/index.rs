use rocket::*;

#[get("/index")]
pub fn index() -> &'static str {
    "Hi, mom!"
}
