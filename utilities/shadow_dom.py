def find_shadow_dom_element(driver, host, element):
        shadow_element = driver.execute_script("""
                    const hostElement = document.getElementById(arguments[0]);
                    const shadowRoot = hostElement.shadowRoot;
                    const shadowElement = shadowRoot.querySelector(arguments[1]);
                    return shadowElement;
            """, host, element)
        return shadow_element

def handle_with_shadow_dom(driver, host, element, operator, input=None):
        if operator == 'click':
            shadow_element = find_shadow_dom_element(driver, host, element)
            driver.execute_script("arguments[0].click();", shadow_element)