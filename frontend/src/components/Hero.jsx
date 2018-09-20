import React from 'react'


const heroStyle = {
    wrapper: {
        borderRadius: "10px",
        backgroundColor: "white",
        padding: "10px",
        marginBottom: "10px",
        overflow: "hidden",
        boxShadow: "1px 1px 2px 2px #ccc8"
    },
    name: {
        float: "left"
    },
    position: {
        float: "left"
    }
}

const heroes = [
    {
        name: "Hanzo",
        position: "Damage"
    },
    {
        name: "Zarya",
        position: "Tank"
    },
    {
        name: "Ana",
        position: "Support"
    }
]

export class Hero extends React.Component {

    render() {
        return (
            <div style={heroStyle.wrapper}>
                <div style={heroStyle.name}>{this.props.data.name}</div>
                <div style={heroStyle.position}>{this.props.data.position}</div>
            </div>
        )
    }
}

export class HeroList extends React.Component {
    render() {
        return (
            heroes.map((item, index) => <Hero key={index} data={item} />)
        )
    }
}