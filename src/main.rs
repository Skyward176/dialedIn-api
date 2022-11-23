// modules

mod routes; // db routes
mod models; //db models
// imports
#[macro_use]
extern crate rocket;
use rocket::{get, http::Status, serde::json::Json};

// sample route
#[get("/")]
fn index() -> Result<Json<String>, Status>{
    Ok(Json(String::from("Hi, mom!")))
}

//launch rocket 
#[launch]
fn rocket() -> _ {
    rocket::build()
        .mount("/", routes![index])
}
