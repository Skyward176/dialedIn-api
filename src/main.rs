#[macro_use] extern crate rocket;

#[get("/")]
fn index() -> &'static str {
    "Hi, mom!"
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![index])
}
