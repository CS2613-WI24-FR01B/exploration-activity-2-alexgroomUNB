
/** @author Alex Groom 3401740
 * 
 */

// project class
class Project {
    constructor(id, name, description, rankedCriteria) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.rankedCriteria = rankedCriteria;
        this.totalWeight = 0;

        for (let i = 0; i < rankedCriteria.length; i++) {
            this.totalWeight += rankedCriteria[i]['weight'];
        }
    }

    totalValue() {
        let totalVal = 0;
        for (let i = 0; i < this.rankedCriteria.length; i++) {
            let relativeWeight = this.rankedCriteria[i]['weight']/this.totalWeight;
            let ranking = this.rankedCriteria[i]['ranking']
            totalVal += relativeWeight*ranking;
        }

        return totalVal;
    }

    criterionWeights() {
        let data = []

        for (let i = 0; i < this.rankedCriteria.length; i++) {
            let percentage = (this.rankedCriteria[i]['weight']/this.totalWeight);

            data.push({
                name: this.rankedCriteria[i]['name'],
                percentage: `${percentage.toFixed(2)}%`
            });
        }

        return data;
    }
}

const fs = require('fs');

class Chart {
    constructor(filePath) {
        this.projects = []
        const jsonIn = fs.readFileSync(filePath, 'utf8');
        const data = JSON.parse(jsonIn);
        for (let i = 0; i <data.length; i++) {
            let proj = new Project(data[i]['id'], data[i]['name'], data[i]['description'], data[i]['criteria_rankings']);
            this.projects.push(proj);
        }
    }

    getLabels() {
        let labels = [];
        for(let i = 0; i < this.projects.length; i++) {
            labels.push(this.projects[i]['name']);
        }

        return labels
    }

    getTotalValues() {
        let totalValues = []
        for(let i = 0; i < this.projects.length; i++) {
            totalValues.push(this.projects[i].totalValue());
        }

        return totalValues;
    }

    chartConfig() {
        const data = {
            type: 'bar',
            data: {
                labels: this.getLabels(),
                datasets: [{
                    label: 'Total Value',
                    data: this.getTotalValues(),
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                  y: {
                    beginAtZero: true
                  }
                }
            }
        };

        return data;
    }
}


const chart = new Chart('database/ProjectObj.json');
const chartConfig = chart.chartConfig();

const data_out = {
    Chart_Config: chartConfig
}
fs.writeFileSync('database/ChartData.json', JSON.stringify(data_out));
console.log('Chart configuration written');
